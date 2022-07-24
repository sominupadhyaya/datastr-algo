const binarySearch = (value , list) =>{
    let first  = 0
    let last  = list.lenght-1
    let position = -1
    let found = false 
    let middle
    while (found === false && first <= last) {
        middle = Math.floor((first+last)/2)
        if(list[middle] === value){
            found = true
            position = middle 
        }
        else if(list[middle] > value){
            last = middle-1
        }else{
            first = middle + 1
        }
    }
    return position
}
const array = [13,12,14,15,28] 

console.log(binarySearch(12,array))

