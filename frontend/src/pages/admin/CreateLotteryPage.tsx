import { observer } from 'mobx-react-lite';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { authStore } from '../../stores/authStore';
import { lotteryAdminStore } from '../../stores/lotteryAdminStore';
import { useNavigate } from 'react-router-dom';
import styles from '../../styles/admin/createLottery.module.scss';
import { useEffect, useState } from 'react';

const validationSchema = Yup.object({
  title: Yup.string()
    .required('Название обязательно')
    .min(1, 'Минимум 1 символ'),
  description: Yup.string()
    .required('Описание обязательно')
    .min(1, 'Минимум 1 символ'),
  // max_count_ticket: Yup.number()
  //   .required('Количество билетов обязательно')
  //   .min(5, 'Минимум 5 билетов'),
  // count_ticket_win: Yup.number()
  //   .required('Количество выигрышных билетов обязательно')
  //   .min(1, 'Минимум 1 выигрышный билет')
  //   .test(
  //     'less-than-max',
  //     'Не может превышать общее количество билетов',
  //     function(value) {
  //       return value <= this.parent.max_count_ticket;
  //     }
  //   ),
  time_start: Yup.string()
    .required('Дата начала обязательна')
    .test(
      'is-future',
      'Дата должна быть в будущем',
      function(value){
        return value ? new Date(value) > new Date() : false;
      }
    )
});

export const CreateLotteryPage = observer(() => {
  const navigate = useNavigate();
  const [isCheckingAuth, setIsCheckingAuth] = useState(true);

  useEffect(()=>{
    const checkAuth = async () => {
      if (!authStore.isAuthenticated){
        await authStore.loadUser();
      }
      setIsCheckingAuth(false);
    };

    checkAuth();
  }, []);

  useEffect(() => {
    if (!isCheckingAuth && !authStore.isAdmin) {
      navigate('/', { replace: true });
    }
  }, [isCheckingAuth, navigate]);

  if (isCheckingAuth || !authStore.isAdmin) {
    return null;
  }

  return (
    <div className={styles["create-lottery-container"]}>
      <h1>Создание новой лотереи</h1>
      
      <Formik
        initialValues={{
          title: '',
          description: '',
          //max_count_ticket: 5,
         // count_ticket_win: 1,
          time_start: ''
        }}
        validationSchema={validationSchema}
        onSubmit={async (values, { setSubmitting }) => {
          try {
            await lotteryAdminStore.createLottery(values);
            navigate('/', {replace: true});
          } finally {
            setSubmitting(false);
          }
        }}
      >
        {({ isSubmitting, setFieldValue }) => (
          <Form className={styles["lottery-form"]}>
            <div className={styles["form-group"]}>
              <label>Название лотереи</label>
              <Field 
                name="title" 
                type="text" 
                className={styles["form-input"]}
                placeholder="Введите название"
              />
              <ErrorMessage name="title" component="div" className={styles["error-message"]} />
            </div>

            <div className={styles["form-group"]}>
              <label>Описание</label>
              <Field 
                name="description" 
                as="textarea" 
                className={styles["form-input textarea"]}
                placeholder="Описание лотереи"
                rows={4}
              />
              <ErrorMessage name="description" component="div" className={styles["error-message"]} />
            </div>

            <div className={styles["form-section"]}>
              {/* <div className={styles["form-group"]}>
                <label>Общее количество билетов</label>
                <Field 
                  name="max_count_ticket" 
                  type="number" 
                  className={styles["form-input"]}
                  placeholder="Введите количество"
                  min="5"
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                    const value = e.target.value;
                    setFieldValue('max_count_ticket', value);
                    if (Number(values.count_ticket_win) > Number(value)) {
                      setFieldValue('count_ticket_win', value);
                    }
                  }}
                />
                <ErrorMessage name="max_count_ticket" component="div" className={styles["error-message"]} />
              </div> */}

              <div className={styles["form-group"]}>
                <label>Дата и время начала</label>
                <Field 
                  name="time_start" 
                  type="datetime-local" 
                  className={styles["form-input"]}
                  step="60" // Шаг 1 минута
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                    setFieldValue('time_start', e.target.value);
                  }}
                />
                <ErrorMessage name="time_start" component="div" className={styles["error-message"]} />
              </div>
              {/* <div className={styles["form-group"]}>
                <label>Количество выигрышных билетов</label>
                <Field 
                  name="count_ticket_win" 
                  type="number" 
                  className={styles["form-input"]}
                  min="1"
                  max={values.max_count_ticket}
                  placeholder="Введите количество"
                />
                <ErrorMessage name="count_ticket_win" component="div" className="error-message" />
              </div> */}
            </div>

            {lotteryAdminStore.error && (
              <div className={styles["form-error"]}>{lotteryAdminStore.error}</div>
            )}

            <div className={styles["form-actions"]}>
              <button 
                type="submit" 
                disabled={isSubmitting || lotteryAdminStore.isLoading}
                className={styles["submit-btn"]}
              >
                {lotteryAdminStore.isLoading ? 'Создание...' : 'Создать лотерею'}
              </button>
              <button
                type="button"
                onClick={() => navigate('/admin/lotteries')}
                className={styles["cancel-btn"]}
              >
                Отмена
              </button>
            </div>
          </Form>
        )}
      </Formik>
    </div>
  );
});