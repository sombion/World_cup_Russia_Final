import { observer } from 'mobx-react-lite';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { authStore } from '../stores/authStore';
import { useNavigate } from 'react-router-dom';
import styles from '../styles/LoginPage.module.scss';

const LoginSchema = Yup.object().shape({
  login: Yup.string().required('Обязательное поле'),
  password: Yup.string().required('Обязательное поле'),
});

export const LoginPage = observer(() => {
  const navigate = useNavigate();

  return (
    <div className={styles["auth-container"]}>
      <div className={styles["auth-card"]}>
        <h1>Вход в систему</h1>
        
        <Formik
          initialValues={{ login: '', password: '' }}
          validationSchema={LoginSchema}
          onSubmit={async (values, { setSubmitting }) => {
            try {
              await authStore.login(values);
              navigate('/');
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            } catch (error) {
              setSubmitting(false);
            }
          }}
        >
          {({ isSubmitting, errors, touched  }) => (
            <Form>
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
                  className={styles["form-input"]} 
                />
                <ErrorMessage name="password" component="div" className={styles["error-message"]} />
              </div>

              {authStore.error && (
                <div className={styles["error-message"]}>{authStore.error}</div>
              )}

              <button 
                type="submit" 
                disabled={isSubmitting || authStore.isLoading}
                className={styles["submit-btn"]}
              >
                {authStore.isLoading ? 'Вход...' : 'Войти'}
              </button>

              <div className={styles["auth-links"]}>
                <span>Нет аккаунта?</span>
                <button 
                  type="button" 
                  onClick={() => navigate('/register')}
                  className={styles["link-btn"]}
                >
                  Зарегистрироваться
                </button>
              </div>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
});