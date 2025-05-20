import type { ReactNode } from 'react';
import { Navbar } from '../components/NavBar/NavBar';


interface WithNavBar {
  children: ReactNode;
}

export const WithNavbar = ({ children }: WithNavBar) => {
  return (
    <>
      <Navbar />
      {children}
    </>
  );
};