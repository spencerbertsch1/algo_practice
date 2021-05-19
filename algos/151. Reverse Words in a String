// 151. Reverse Words in a String - javascript

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // split this into many strings! 
    const s_list = s.split(" ")
    
    const hard_way_list = []
    
    // the long way 
    for (let i = s_list.length-1; i>=0; i--){
        if (s_list[i] !== '') {
            hard_way_list.push(s_list[i])
        }
    }
    
    const joined_list = hard_way_list.join(' ')
    
    return joined_list
    
};
