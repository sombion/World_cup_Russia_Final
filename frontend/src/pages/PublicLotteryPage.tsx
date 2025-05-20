// // src/pages/PublicLotteriesPage.tsx
// import { observer } from 'mobx-react-lite';
// import { useEffect, useState } from 'react';
// import { lotteryPublicStore } from '../stores/lotteryPublicStore';
// import '../styles/publicLotteries.module.scss';

// export const PublicLotteriesPage = observer(() => {
//   const [titleFilter, setTitleFilter] = useState('');
//   const [startDateFilter, setStartDateFilter] = useState('');

//   useEffect(() => {
//     lotteryPublicStore.fetchLotteries();
//   }, []);

//   const handleFilter = () => {
//     lotteryPublicStore.setFilter({
//       title: titleFilter,
//       startDate: startDateFilter
//     });
//   };

//   const handleResetFilters = () => {
//     setTitleFilter('');
//     setStartDateFilter('');
//     lotteryPublicStore.setFilter({});
//   };

//   const formatDate = (dateString: string) => {
//     return format(new Date(dateString), 'dd.MM.yyyy HH:mm', { locale: ru });
//   };

//   return (
//     <div className="public-lotteries-container">
//       <h1>Доступные лотереи</h1>
      
//       <div className="filters">
//         <div className="filter-group">
//           <label>Поиск по названию:</label>
//           <input
//             type="text"
//             value={titleFilter}
//             onChange={(e) => setTitleFilter(e.target.value)}
//             placeholder="Введите название"
//           />
//         </div>
        
//         <div className="filter-group">
//           <label>Дата начала после:</label>
//           <input
//             type="date"
//             value={startDateFilter}
//             onChange={(e) => setStartDateFilter(e.target.value)}
//           />
//         </div>
        
//         <div className="filter-actions">
//           <button onClick={handleFilter}>Применить фильтры</button>
//           <button onClick={handleResetFilters}>Сбросить</button>
//         </div>
//       </div>

//       {lotteryPublicStore.error && (
//         <div className="error-message">{lotteryPublicStore.error}</div>
//       )}

//       {lotteryPublicStore.isLoading ? (
//         <div className="loading">Загрузка...</div>
//       ) : (
//         <div className="lotteries-grid">
//           {lotteryPublicStore.lotteries.map((lottery) => (
//             <div key={lottery.id} className="lottery-card">
//               <h3>{lottery.title}</h3>
//               <p className="description">{lottery.description}</p>
              
//               <div className="details">
//                 <div>
//                   <span>Билетов всего:</span>
//                   <strong>{lottery.max_count_ticket}</strong>
//                 </div>
//                 <div>
//                   <span>Выигрышных билетов:</span>
//                   <strong>{lottery.count_ticket_win}</strong>
//                 </div>
//                 <div>
//                   <span>Начало:</span>
//                   <strong>{formatDate(lottery.time_start)}</strong>
//                 </div>
//               </div>
              
//               <button className="participate-btn">
//                 Участвовать
//               </button>
//             </div>
//           ))}
//         </div>
//       )}
//     </div>
//   );
// });