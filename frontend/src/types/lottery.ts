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

export interface LotteriesFilter {
  title?: string;
  startDate?: string;
}