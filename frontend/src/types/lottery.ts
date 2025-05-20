export interface LotteryCreateForm{
    title: string;
    description: string;
   // max_count_ticket: number;
   // count_ticket_win: number;
    time_start: string;
}

export interface Lottery {
  id: string;
  title: string;
  description: string;
  max_count_ticket: number;
 // count_ticket_win: number;
  time_start: string; // ISO format
  //created_at: string;
}

export interface LotteryList{
  id: number;
  title: string;
  description: string;
  price_ticket: number;
  accumulation: string | null;
  time_start: string;
  time_end: string;
  win_time: string | null;
}

export interface LotteryListResponse{
  lotterys: LotteryList[];
}

export interface LotteriesFilter {
  title?: string;
  startDate?: string;
}

export interface LotteryDetails {
    id: number;
    title: string;
    description: string;
    accumulation: number | null;
    time_end: string;
    price_ticket: number;
    time_start: string;
    win_time: string;
    ticket_count: number;
}