
// import './search.css';

import React, { useState, useEffect } from "react";
import { FaTimes } from 'react-icons/fa';

const url = "http://localhost:8000/phuongtien/search/?format=json&q="

const Search = () => {

  const [isLoading,setIsLoading] = useState(true)
  const [isError,setIsError] = useState(false)
  const [users,setUsers] = useState([])
  const [q,setQ] = useState('Xe c')

  useEffect(() => {
    fetch(url+q)
      .then(response => {
        if(response.status === 200) {
          
          return response.json();
        }
        setIsError(true)
      })
      .then(data => {
        if (!isError) {
          setTimeout(() => {
            setUsers(data)
            setIsLoading(false)
          }, 100);
        }
      })
  },[isLoading])

  const deleteItem = (pk) =>{
    console.log(users)
    let newUsers = users.filter(user => {
      if (user.pk !== pk) {
        return user
      }
    })
    setUsers(newUsers)
  }

  return <>
  <div className="search-bar">
    <h3>Tìm kiếm phương tiện</h3>
    <input type="text" value={q} onChange={(e) => { setQ(e.target.value)} }/>
    <button className="btn" 
      onClick={() => {
        setIsLoading(true)
        setUsers([])
      }}>
        Tìm kiếm
    </button>
    <h4>{users.length}</h4>
  </div>

  <div className='results'>
    { users.map(user => {
      const {ten, chung_loai, nhan_hieu, hinh_anh } = user.fields
      const {pk} = user
      return (
        <div className="result-item" key={pk}>
          <img src={hinh_anh} alt=""/>
          <div>
            <p>{ten}</p>
            <a href={pk}>{chung_loai}</a>
            <a href={pk}>{nhan_hieu}</a>
          </div>
          <button className='close-modal-btn' onClick={()=>deleteItem(pk)}>
          <FaTimes></FaTimes>
        </button>
        </div>
      )
   })}
  </div>
  </>
}

export default Search;