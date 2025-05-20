import { makeAutoObservable, runInAction } from 'mobx';
import axios from 'axios';
import { type LotteryCreateForm } from '../types/lottery';


export class LotteryAdminStore {
  isLoading = false;
  error: string | null = null;

  constructor() {
    makeAutoObservable(this);
  }

  async createLottery(lotteryData: LotteryCreateForm) {
    this.isLoading = true;
    this.error = null;
    
    try {
      const formattedData = {
        ...lotteryData,
        time_start: new Date(lotteryData.time_start).toISOString()
      };
      
      await axios.post('/api/lottery/create', formattedData);
      return true;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      this.error = error.response?.data?.detail || 'Ошибка при создании лотереи';
      return false;
    } finally {
      runInAction(()=>{
        this.isLoading = false;
      })
    }
  }
}
export const lotteryAdminStore = new LotteryAdminStore();