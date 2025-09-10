function transform(str) {
    let result = "";

    for (let i = 0; i < str.length; i++) {
        let ch = str[i];
        if (/[A-Z]/.test(ch)) {
            // Uppercase letters → shift by +5
            let base = 'A'.charCodeAt(0);
            let newChar = String.fromCharCode(((ch.charCodeAt(0) - base + 5) % 26) + base);
            result += newChar;
        } else if (/[a-z]/.test(ch)) {
            // Lowercase letters → shift by +5
            let base = 'a'.charCodeAt(0);
            let newChar = String.fromCharCode(((ch.charCodeAt(0) - base + 5) % 26) + base);
            result += newChar;
        } else {
            // Non-alphabetic characters remain same
            result += ch;
        }
    }

    return result;
}

// Test
console.log(transform("xtD"));  
