// src/pages/LotteryDetailsPage.tsx
import { observer } from 'mobx-react-lite';
import { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { lotteryPublicStore } from '../stores/lotteryPublicStore';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import styles from '../styles/lotteryDetails.module.scss';

export const LotteryDetailsPage = observer(() => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const lottery = lotteryPublicStore.currentLottery;

  
  useEffect(() => {
    if (id) {
      lotteryPublicStore.fetchLotteryDetails(parseInt(id));
    }
  }, [id]);

  const handleBuyTicket = async () => {
    if (!lottery) return;
    
    const success = await lotteryPublicStore.buyTicket(lottery.id);
    if (success) {
      navigate('/lotteries');
    }
  };

  const formatDate = (isoString: string) => {
    const date = new Date(isoString);
    return date.toLocaleString('ru-RU');
  };

  if (lotteryPublicStore.isLoading || !lottery) {
    return <div className={styles["loading"]}>Загрузка...</div>;
  }

  return (
    <div className={styles["lottery-details-container"]}>
      <Formik
        initialValues={{ ticketCount: 1 }}
        onSubmit={handleBuyTicket}
      >
        {({ isSubmitting }) => (
          <Form className={styles["lottery-form"]}>
            <h1>{lottery.title}</h1>
            
            <div className={styles["lottery-info"]}>
              <div className={styles["description-section"]}>
                <h2>Описание</h2>
                <p>{lottery.description}</p>
              </div>

              <div className={styles["details-grid"]}>
                <div className={styles["detail-item"]}>
                  <span>Начало:</span>
                  <strong>{formatDate(lottery.time_start)}</strong>
                </div>
                <div className={styles["detail-item"]}>
                  <span>Окончание:</span>
                  <strong>{formatDate(lottery.time_end)}</strong>
                </div>
                <div className={styles["detail-item"]}>
                  <span>Цена билета:</span>
                  <strong>{lottery.price_ticket} ₽</strong>
                </div>
                <div className={styles["detail-item"]}>
                  <span>Продано билетов:</span>
                  <strong>{lottery.ticket_count}</strong>
                </div>
              </div>

              <div className={styles["form-section"]}>
                <label htmlFor="ticketCount">Количество билетов:</label>
                <Field 
                  name="ticketCount" 
                  type="number" 
                  min="1" 
                  className={styles["form-input"]}
                />
                <ErrorMessage name="ticketCount" component="div" className={styles["error"]} />
              </div>

              <button 
                type="submit" 
                disabled={isSubmitting || lotteryPublicStore.buyLoading}
                className={styles["submit-btn"]}
              >
                {lotteryPublicStore.buyLoading ? 'Покупка...' : 'Купить билет'}
              </button>

              {lotteryPublicStore.buyError && (
                <div className={styles["error-message"]}>{lotteryPublicStore.buyError}</div>
              )}
            </div>
          </Form>
        )}
      </Formik>
    </div>
  );
});