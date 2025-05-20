// src/stores/lotteryPublicStore.ts
import { makeAutoObservable, runInAction } from 'mobx';
import axios from 'axios';
import type { LotteryList, LotteriesFilter, LotteryDetails, LotteryListResponse } from '../types/lottery';

export class LotteryPublicStore {
  isLoading = false;
  error: string | null = null;
  lotteries: LotteryList[] = [];
  filter: LotteriesFilter = {};
  currentLottery: LotteryDetails | null = null;
  buyLoading = false;
  buyError: string | null = null;


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

      const response = await axios.get<LotteryListResponse>(`/api/lottery/all?${params.toString()}`);
      runInAction(() => {
        this.lotteries = response.data.lotterys;
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

  async fetchLotteryDetails(id: number) {
    this.isLoading = true;
    this.error = null;
    
    try {
      const response = await axios.get(`/api/lottery/detail/${id}`);
      runInAction(() => {
        this.currentLottery = response.data;
      });
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      runInAction(() => {
        this.error = error.response?.data?.detail || 'Ошибка загрузки лотереи';
      });
    } finally {
      runInAction(() => {
        this.isLoading = false;
      });
    }
  }

  async buyTicket(lotteryId: number, ticketCount: number = 1) {
    this.buyLoading = true;
    this.buyError = null;
    
    try {
      await axios.post('/api/ticket/buy', { 
        lottery_id: lotteryId,
        count: ticketCount
      });
      return true;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    } catch (error: any) {
      runInAction(() => {
        this.buyError = error.response?.data?.detail || 'Ошибка покупки билета';
      });
      return false;
    } finally {
      runInAction(() => {
        this.buyLoading = false;
      });
    }
  }

  setFilter(filter: LotteriesFilter) {
    this.filter = filter;
    this.fetchLotteries();
  }
}

export const lotteryPublicStore = new LotteryPublicStore();