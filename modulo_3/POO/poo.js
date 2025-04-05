class Car {
  constructor(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
  }

  start() {
    console.log(`Starting ${this.brand} ${this.model}`);
  }

  stop() {
    console.log(`Stopping ${this.brand} ${this.model}`);
  }
}

carro1 = new Car("Toyota", "Corolla", 2020);
carro2 = new Car("Honda", "Civic", 2021);
carro3 = new Car("Ford", "Mustang", 2022);
carro4 = new Car("Chevrolet", "Camaro", 2023);

carro1.start();
console.log(carro2.brand);
