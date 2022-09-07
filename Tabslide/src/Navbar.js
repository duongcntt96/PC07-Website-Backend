
import { useState, useEffect } from "react";

const data = [
    { title: "Trang chủ", url: "#1" },
    { title: "Quản lý phương tiện", url: "#2",
        sub: [
            { title: "Sub 3", url: "#sub1"},{ title: "Phương tiện theo tổ", url: "#sub1"},
            { title: "Phương tiện theo chủng loại", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
          
        ]
    },
    { title: "Bộ máy tổ chức", url: "#2",
        sub: [
            { title: "Lịch sử hình thành và phát triển", url: "#sub1"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
            { title: "Sub 4", url: "#sub2"},
        ]
    },
    // { title: "Góp ý", url: "#2" },
]

const Navbar = () => {

    const [links, setLinks] = useState(data)
    const [subLink, setSubLink] = useState([])

    return <>
    <div className="header">
        <img src="" alt="logo" className="logo"/>
        <ul className="links">
            { links.map(item => {
                const {title, url, sub} = item
                return <div className="link-item" onMouseOver={()=>setSubLink(sub?sub:[])}>
                    <a href={url}>{title}</a>
                </div>
            })}
        </ul>
           <ul className="sub-links">
            {subLink.map(link => {
                const {title, url} = link
                return <li className="sub-link-item">
                    <a href={url}>{title}</a>
                </li>
            })}
        </ul>
    </div>
 
    </>
}

export default Navbar;