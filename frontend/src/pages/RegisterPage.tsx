import { observer } from 'mobx-react-lite';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { authStore } from '../stores/authStore';
import { useNavigate } from 'react-router-dom';
import styles from '../styles/RegisterPage.module.scss';

const RegisterSchema = Yup.object().shape({
  username: Yup.string().required('Обязательное поле'),
  login: Yup.string().required('Обязательное поле'),
  password: Yup.string()
    .min(6, 'Не менее 6 символов!')
    .required('Обязательное поле'),
  is_admin: Yup.boolean().required('Обязательное поле'),
});

export const RegisterPage = observer(() => {
  const navigate = useNavigate();

  return (
    <div className={styles["auth-container"]}>
      <div className={styles["auth-card"]}>
        <h1>Регистрация</h1>
        
        <Formik
          initialValues={{ 
            username: '', 
            login: '', 
            password: '',
            is_admin: false,
          }}
          validationSchema={RegisterSchema}
          onSubmit={async (values, { setSubmitting }) => {
            try {
              await authStore.register(values);
              navigate('/');
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            } catch (error) {
              setSubmitting(false);
            }
          }}
        >
          {({ isSubmitting, errors, touched }) => (
            <Form>
              <div className={`${styles["form-group"]} ${errors.username && touched.username ? styles["has-error"] : ""}`}>
                <label htmlFor="username">ФИО</label>
                <Field 
                  type="text" 
                  name="username" 
                  id="username" 
                  className={styles['form-input']} 
                />
                <ErrorMessage name="username" component="div" className={styles['error-message']} />
              </div>

              <div className={`${styles["form-group"]} ${errors.login && touched.login ? styles["has-error"] : ""}`}>
                <label htmlFor="login">Логин</label>
                <Field 
                  type="text" 
                  name="login" 
                  id="login" 
                  className={styles['form-input']} 
                />
                <ErrorMessage name="login" component="div" className={styles['error-message']} />
              </div>
          
              <div className={`${styles["form-group"]} ${errors.password && touched.password ? styles["has-error"] : ""}`}>
                <label htmlFor="password">Пароль</label>
                <Field 
                  type="password" 
                  name="password" 
                  id="password" 
                  className={styles['form-input']} 
                />
                <ErrorMessage name="password" component="div" className={styles['error-message']} />
              </div>

              <div className={`${styles["form-group"]} ${errors.is_admin && touched.is_admin ? styles["has-error"] : ""}`}>
                <label className={styles['form-checkbox']}>
                <Field 
                  type="checkbox" 
                  name="is_admin" 
                  id="is_admin" 
                />
                <span>Администратор</span>
                </label>
                <ErrorMessage name="is_admin" component="div" className={styles['error-message']} />
              </div>

              {authStore.error && (
                <div className={styles['error-message']}>{authStore.error}</div>
              )}

              <button 
                type="submit" 
                disabled={isSubmitting || authStore.isLoading}
                className={styles['submit-btn']}
              >
                {authStore.isLoading ? 'Регистрация...' : 'Зарегистрироваться'}
              </button>
          
              <div className={styles['auth-links']}>
                <span>Уже есть аккаунт?</span>
                <button 
                  type="button" 
                  onClick={() => navigate('/login')}
                  className={styles['link-btn']}
                >
                  Войти
                </button>
              </div>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
});