// src/types/me.ts
export interface IUser {
  id: number;
  username: string;
  login: string;
  hash_password: string;
  is_admin: boolean;
  money: number;
  // Остальные поля, если они нужны в Navbar
  xp?: number;
  lvl?: number;
  cube?: number;
  ruby?: number;
}