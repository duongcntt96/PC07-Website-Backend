import React, {useState} from 'react';
import { useGlobalContext } from './context';
import { FaTimes } from 'react-icons/fa';
const Modal = () => {

  const { isModalOpen, closeModal, login } = useGlobalContext();
  const [username,setUsername] = useState('');
  const [password,setPassword] = useState('');
  return (
    <div
      className={`${
        isModalOpen ? 'modal-overlay show-modal' : 'modal-overlay'
      }`}
    >
      <div className='modal-container'>
        <form className='modal-container' action="" onSubmit={(e) => login(e,username,password)}>
          <br></br>
          <input type="text" className="username" placeholder=" Tên đăng nhập" value={username} onChange={(e) => setUsername(e.target.value)}/>
          <input type="password" className="username" placeholder=" Mật khẩu" value={password} onChange={(e) => setPassword(e.target.value)}/>
          
          <button className="btn" type="submit">Đăng nhập</button>
        </form>
        <button className='close-modal-btn' onClick={closeModal}>
          <FaTimes></FaTimes>
        </button>
      </div>
    </div>
  );
};

export default Modal;
