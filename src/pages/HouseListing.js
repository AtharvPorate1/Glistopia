import React from 'react'
import { useState,useEffect } from 'react'
import ListItem from '../components/ListItem'

const HouseListing = () => {
    let [housing, setHousing] = useState([])

    useEffect(() => {
        getHousing()
    }, [])


    let getHousing = async () => {

        let response = await fetch('http://127.0.0.1:8000/housing/')
        let data = await response.json()
        setHousing(data)
    }

  return (
    <div>
      House Listings
      <div className="notes">
            <div className="notes-header">
                {/* <h2 className="notes-title">&#9782; House Listing</h2> */}
                <p className="notes-count">{housing.length}</p>
            </div>

            <div className="notes-list">
                {housing.map((housing, index) => (
                    
                    <ListItem key={index} housing={housing}/>
                ))}
            </div>
            
        </div>
      
    </div>
  )
}

export default HouseListing
