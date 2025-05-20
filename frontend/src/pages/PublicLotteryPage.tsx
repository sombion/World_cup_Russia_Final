// src/pages/PublicLotteriesPage/PublicLotteriesPage.tsx
import React, { useEffect } from 'react';
import { observer } from 'mobx-react-lite';
import { lotteryPublicStore } from '../stores/lotteryPublicStore';
import { LotteryCard } from '../components/LotteryCard/LotteryCard';
import styles from '../styles/publicLotteries.module.scss';

const PublicLotteriesPage: React.FC = observer(() => {
  useEffect(() => {
    lotteryPublicStore.fetchLotteries();
  }, []);

  const handleBuyTicket = async (lotteryId: number) => {
    return await lotteryPublicStore.buyTicket(lotteryId);
  };

  if (lotteryPublicStore.isLoading && !lotteryPublicStore.lotteries.length) {
    return <div className={styles.loading}>Загрузка лотерей...</div>;
  }

  if (lotteryPublicStore.error) {
    return <div className={styles.error}>{lotteryPublicStore.error}</div>;
  }

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Публичные лотереи</h1>
      
      <div className={styles.filters}>
        <input
          type="text"
          placeholder="Поиск по названию"
          onChange={(e) => lotteryPublicStore.setFilter({ title: e.target.value })}
          className={styles.searchInput}
        />
        <input
          type="date"
          onChange={(e) => lotteryPublicStore.setFilter({ startDate: e.target.value })}
          className={styles.dateInput}
        />
      </div>

      <div className={styles.grid}>
        {lotteryPublicStore.lotteries.map((lottery) => (
          <LotteryCard
            key={lottery.id}
            lottery={lottery}
            onBuy={handleBuyTicket}
            isBuying={lotteryPublicStore.buyLoading}
            buyError={lotteryPublicStore.buyError}
          />
        ))}
      </div>

      {!lotteryPublicStore.isLoading && lotteryPublicStore.lotteries.length === 0 && (
        <div className={styles.empty}>Лотереи не найдены</div>
      )}
    </div>
  );
});

export default PublicLotteriesPage;