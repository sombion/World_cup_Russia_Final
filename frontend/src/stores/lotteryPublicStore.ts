// src/stores/lotteryPublicStore.ts
import { makeAutoObservable, runInAction } from 'mobx';
import axios from 'axios';
import type { Lottery, LotteriesFilter } from '../types/lottery';

export class LotteryPublicStore {
  isLoading = false;
  error: string | null = null;
  lotteries: Lottery[] = [];
  filter: LotteriesFilter = {};

  constructor() {
    makeAutoObservable(this);
  }

  async fetchLotteries() {
    this.isLoading = true;
    this.error = null;
    
    try {
      const params = new URLSearchParams();
      if (this.filter.title) params.append('title', this.filter.title);
      if (this.filter.startDate) params.append('start_date', this.filter.startDate);

      const response = await axios.get(`/api/lottery/all?${params.toString()}`);
      runInAction(() => {
        this.lotteries = response.data;
      });
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      runInAction(() => {
        this.error = error.response?.data?.detail || 'Ошибка загрузки лотерей';
      });
    } finally {
      runInAction(() => {
        this.isLoading = false;
      });
    }
  }

  setFilter(filter: LotteriesFilter) {
    this.filter = filter;
    this.fetchLotteries();
  }
}

export const lotteryPublicStore = new LotteryPublicStore();