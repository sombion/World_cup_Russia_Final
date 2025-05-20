// // src/stores/store.ts
// import { LotteryAdminStore } from './lotteryAdminStore';
// import { authStore } from './userStore';
// import { LotteryStore } from './lotteryAdminStore';

// export class RootStore {
//   authStore: UserStore;
//   lotteryStore: LotteryStore;
//   lotteryAdminStore: LotteryAdminStore;

//   constructor() {
//     this.authStore = new AuthStore(this);
//     this.lotteryStore = new LotteryStore(this);
//     this.lotteryAdminStore = new LotteryAdminStore(this);
//   }
// }

// export const rootStore = new RootStore();

// export const useStore = () => rootStore;