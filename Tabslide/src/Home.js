import React from 'react';
import { FaBars } from 'react-icons/fa';
import { useGlobalContext } from './context';
import logo from './logo.jpg';

import Search from './phuongtien/Search';

const Home = () => {
  const { openSidebar, openModal } = useGlobalContext();
  return (
    <main>
      
      <button onClick={openSidebar} className='sidebar-toggle' style={{backgroundColor: 'white'}}>
      <img src={logo} className='logo' alt='coding addict' />
      </button>
      
<Search />
{/* <button onClick={openModal} className='btn'>
        show modal
      </button> */}
    </main>
  );
};

export default Home;
