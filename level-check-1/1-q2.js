function gcd(a, b) {
    var tmp = 0;

    if (a < b) {
        tmp = a;
        a = b;
        b = tmp;
    }

    while(b !== 0) {
        tmp = a%b;
        a = b;
        b = tmp;
    }

    return a;
}

function lcm(a, b) {
    return a*b/gcd(a, b);
}

function solution(n, m) {
    var answer = [];
    answer.push(gcd(n,m))
    answer.push(lcm(n,m))
    return answer;
}
