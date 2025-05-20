import { makeAutoObservable } from 'mobx';
import axios from 'axios';
import type { IUser, IAuthResponse, IRegisterForm, ILoginForm } from '../types/auth';

class AuthStore {
  user: IUser | null = null;
  isLoading = false;
  error: string | null = null;

  constructor() {
    makeAutoObservable(this);
    this.initializeAuth();
  }

  private initializeAuth() {
    const token = localStorage.getItem('access_token');
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      this.loadUser();
    }
  }

  async loadUser() {
    this.isLoading = true;
    try {
      const response = await axios.get<IUser[]>('/api/auth/me');
      this.user = response.data[0];
    } catch (error) {
      this.user = null;
      console.error('Ошибка загрузки пользователя:', error);

    } finally {
      this.isLoading = false;
    }
  }

  async register(formData: IRegisterForm) {
    try {
      this.isLoading = true;
      await axios.post('/api/auth/register', formData);
      await this.login({
        login: formData.login,
        password: formData.password
      });
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      this.error = error.response?.data?.detail || 'Ошибка регистрации';
      throw error;
    } finally {
      this.isLoading = false;
    }
  }

  async login(formData: ILoginForm) {
    try {
      this.isLoading = true;
      const response = await axios.post<IAuthResponse>('/api/auth/login', formData);
      this.user = response.data.user;
      localStorage.setItem('access_token', response.data.access_token);
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access_token}`;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      this.error = error.response?.data?.detail || 'Ошибка авторизации';
      throw error;
    } finally {
      this.isLoading = false;
    }
  }

  logout() {
    this.user = null;
    localStorage.removeItem('access_token');
    axios.defaults.headers.common['Authorization'] = '';
  }

  get isAuthenticated() {
    return !!this.user;
  }

  get isAdmin() {
    return this.user?.is_admin || false;
  }
}

export const authStore = new AuthStore();