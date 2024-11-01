import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [items, setItems] = useState(null)

  const fetchItems = () => {
    axios.get('https://194.247.187.229/api/items').then(r => {
      setItems(r.data)
    })
  }

  useEffect(() => {
    fetchItems()
    setInterval(() => {
      fetchItems()
    }, 2000)
  }, [])

  return (
    <>
      {items && items.map(item => {
        return <span style={{padding:'0px 4px'}} key={item.name} className="roll-out">
          <img src={item.img} alt='logo' width="40" style={{padding:'0px 5px'}}></img>
          <span>{item.name}</span>
        </span>
      })}
    </>
  )
}

export default App
