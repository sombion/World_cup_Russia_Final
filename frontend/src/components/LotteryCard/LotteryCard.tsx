// src/components/LotteryCard/LotteryCard.tsx
import React from 'react';
import { observer } from 'mobx-react-lite';
import type { LotteryList } from '../../types/lottery';
import styles from './LotteryCard.module.scss';

interface LotteryCardProps {
  lottery: LotteryList;
  onBuy: (lotteryId: number) => Promise<boolean>;
  isBuying: boolean;
  buyError?: string | null;
}

export const LotteryCard: React.FC<LotteryCardProps> = observer(({
  lottery,
  onBuy,
  isBuying,
  buyError
}) => {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleString('ru-RU', {
      day: 'numeric',
      month: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const handleBuy = async () => {
    await onBuy(lottery.id);
  };

  return (
    <div className={styles.card}>
      <div className={styles.header}>
        <h3 className={styles.title}>{lottery.title}</h3>
        <div className={styles.price}>{lottery.price_ticket} ₽</div>
      </div>
      
      <p className={styles.description}>{lottery.description}</p>
      
      <div className={styles.details}>
        <div className={styles.detailItem}>
          <span className={styles.detailLabel}>Начало:</span>
          <span>{formatDate(lottery.time_start)}</span>
        </div>
        <div className={styles.detailItem}>
          <span className={styles.detailLabel}>Окончание:</span>
          <span>{formatDate(lottery.time_end)}</span>
        </div>
        {lottery.accumulation && (
          <div className={styles.detailItem}>
            <span className={styles.detailLabel}>Призовой фонд:</span>
            <span className={styles.accumulation}>{lottery.accumulation}</span>
          </div>
        )}
      </div>

      <button
        onClick={handleBuy}
        disabled={isBuying}
        className={styles.buyButton}
      >
        {isBuying ? 'Покупка...' : 'Купить билет'}
      </button>
      
      {buyError && <div className={styles.error}>{buyError}</div>}
    </div>
  );
});