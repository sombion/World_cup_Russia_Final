// types/auth.ts
export interface IUser {
  id: number;
  username: string;
  login: string;
  is_admin: boolean;
  money: number;
}

export interface IAuthResponse {
  user: IUser;
  access_token: string;
}

export interface IRegisterForm {
  username: string;
  login: string;
  password: string;
  is_admin: boolean;
}

export interface ILoginForm {
  login: string;
  password: string;
}