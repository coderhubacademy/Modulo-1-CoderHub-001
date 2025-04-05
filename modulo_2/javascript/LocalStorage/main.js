var first_users = [
  {
    name: "John Doe",
    lastname: "Doe",
    email: "john.doe@test.com",
    phone: 1234556,
    country: "US",
  },
  {
    name: "Pedro",
    lastname: "Perez",
    email: "pedro.perez@test.com",
    phone: 2345678,
    country: "MX",
  },
];

localStorage.setItem("users", JSON.stringify(first_users));

function showUsers() {
  let users = JSON.parse(localStorage.getItem("users"));
  console.log("Users", users);
  let user_list = document.getElementById("user-list");
  users.forEach((user) => {
    let table_row = document.createElement("tr");
    let table_name = document.createElement("td");
    table_name.innerText = user.name;
    let table_lastname = document.createElement("td");
    table_lastname.innerText = user.lastname;
    let table_email = document.createElement("td");
    table_email.innerText = user.email;
    let table_phone = document.createElement("td");
    table_phone.innerText = user.phone;
    let table_country = document.createElement("td");
    table_country.innerText = user.country;

    table_row.appendChild(table_name);
    table_row.appendChild(table_lastname);
    table_row.appendChild(table_email);
    table_row.appendChild(table_phone);
    table_row.appendChild(table_country);

    user_list.appendChild(table_row);
  });
}

showUsers();
