class User {
    constructor () {
        this.name = '';
        this.token = '';
        this.city = '';
        this.email = '';
        this.isLoggedIn = false;
    }

    isLoggedIn () {
        return this.isLoggedIn;
    }

    toggleLoggedIn () {
        this.isLoggedIn = !this.isLoggedIn;
    }

    getName () {
        return this.name;
    }

    getToken () {
        return this.token;
    }

    getCity () {
        return this.city;
    }

    getEmail () {
        return this.email;
    }

    setName (name) {
        this.name = name;
        return this;
    }

    setToken (token) {
        this.token = token;
        return this;
    }

    setEmail (email) {
        this.email = email;
        return this;
    }
}

const user = new User();
export default user;
