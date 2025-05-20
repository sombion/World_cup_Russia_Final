// src/pages/LotteryDetailsPage.tsx
import { observer } from 'mobx-react-lite';
import { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { lotteryPublicStore } from '../stores/lotteryPublicStore';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import '../styles/lotteryDetails.module.scss';

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
      navigate('/');
    }
  };

  const formatDate = (isoString: string) => {
    const date = new Date(isoString);
    return date.toLocaleString('ru-RU');
  };

  if (lotteryPublicStore.isLoading || !lottery) {
    return <div className="loading">Загрузка...</div>;
  }

  return (
    <div className="lottery-details-container">
      <Formik
        initialValues={{ ticketCount: 1 }}
        onSubmit={handleBuyTicket}
      >
        {({ isSubmitting }) => (
          <Form className="lottery-form">
            <h1>{lottery.title}</h1>
            
            <div className="lottery-info">
              <div className="description-section">
                <h2>Описание</h2>
                <p>{lottery.description}</p>
              </div>

              <div className="details-grid">
                <div className="detail-item">
                  <span>Начало:</span>
                  <strong>{formatDate(lottery.time_start)}</strong>
                </div>
                <div className="detail-item">
                  <span>Окончание:</span>
                  <strong>{formatDate(lottery.time_end)}</strong>
                </div>
                <div className="detail-item">
                  <span>Цена билета:</span>
                  <strong>{lottery.price_ticket} ₽</strong>
                </div>
                <div className="detail-item">
                  <span>Продано билетов:</span>
                  <strong>{lottery.ticket_count}</strong>
                </div>
              </div>

              <div className="form-section">
                <label htmlFor="ticketCount">Количество билетов:</label>
                <Field 
                  name="ticketCount" 
                  type="number" 
                  min="1" 
                  className="form-input"
                />
                <ErrorMessage name="ticketCount" component="div" className="error" />
              </div>

              <button 
                type="submit" 
                disabled={isSubmitting || lotteryPublicStore.buyLoading}
                className="submit-btn"
              >
                {lotteryPublicStore.buyLoading ? 'Покупка...' : 'Купить билет'}
              </button>

              {lotteryPublicStore.buyError && (
                <div className="error-message">{lotteryPublicStore.buyError}</div>
              )}
            </div>
          </Form>
        )}
      </Formik>
    </div>
  );
});