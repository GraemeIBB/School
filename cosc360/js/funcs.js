function basic() {
    return "classic";
}

const anon = () => "example"

const anon2 = a => `ex${a}mple`

const anon3 = (a, b) => {
    console.log("bazinga");
    console.log(a + b);
}

const anon4 = () => anon2("b")


