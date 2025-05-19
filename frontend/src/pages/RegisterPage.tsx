import { observer } from 'mobx-react-lite';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { authStore } from '../stores/authStore';
import { useNavigate } from 'react-router-dom';
import '../styles/auth.scss';

const RegisterSchema = Yup.object().shape({
  username: Yup.string().required('Обязательное поле'),
  login: Yup.string().required('Обязательное поле'),
  password: Yup.string()
    .min(6, 'Пароль должен быть не менее 6 символов')
    .required('Обязательное поле'),
  is_admin: Yup.boolean().required('Обязательное поле'),
});

export const RegisterPage = observer(() => {
  const navigate = useNavigate();

  return (
    <div className="auth-container">
      <div className="auth-card">
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
          {({ isSubmitting }) => (
            <Form>
              <div className="form-group">
                <label htmlFor="username">ФИО</label>
                <Field 
                  type="text" 
                  name="username" 
                  id="username" 
                  className="form-input" 
                />
                <ErrorMessage name="username" component="div" className="error-message" />
              </div>

              <div className="form-group">
                <label htmlFor="login">Логин</label>
                <Field 
                  type="text" 
                  name="login" 
                  id="login" 
                  className="form-input" 
                />
                <ErrorMessage name="login" component="div" className="error-message" />
              </div>

              <div className="form-group">
                <label htmlFor="password">Пароль</label>
                <Field 
                  type="password" 
                  name="password" 
                  id="password" 
                  className="form-input" 
                />
                <ErrorMessage name="password" component="div" className="error-message" />
              </div>

              <div className="form-group">
                <label htmlFor="is_admin">Администратор?</label>
                <Field 
                  type="checkbox" 
                  name="is_admin" 
                  id="is_admin" 
                  className="form-input" 
                />
                <ErrorMessage name="is_admin" component="div" className="error-message" />
              </div>

              {authStore.error && (
                <div className="error-message">{authStore.error}</div>
              )}

              <button 
                type="submit" 
                disabled={isSubmitting || authStore.isLoading}
                className="submit-btn"
              >
                {authStore.isLoading ? 'Регистрация...' : 'Зарегистрироваться'}
              </button>

              <div className="auth-links">
                <span>Уже есть аккаунт?</span>
                <button 
                  type="button" 
                  onClick={() => navigate('/login')}
                  className="link-btn"
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