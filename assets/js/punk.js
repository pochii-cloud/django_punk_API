document.addEventListener('DOMContentLoaded',()=>{
    const  startBtn=document.querySelector('.beer-button')
    const  randomBeer=document.querySelector('.random-beer')
    const  descriptionDisplay=document.querySelector('.description')
    const  getimage=document.querySelector('.beer-image')
    function getData(e) {
        e.preventDefault()
        fetch('https://api.punkapi.com/v2/beers/random')
            .then(response => {
                return response.json()
            })
            .then(data => {
                const name = data[0].name
                const description = data[0].description
                const image_url=data[0].imageURL
                const {volume} = data[0]
                const volumeValue = volume.value
                const volumeUnit = volume.unit

                randomBeer.innerHTML = name + '' + volumeValue + volumeUnit
                descriptionDisplay.innerHTML = description
                getimage.innerHTML= beer-image
            })
    }
    startBtn.addEventListener('click',getData)
})