let cupcakes = [];

function showCupcakes(cupcakes) {
  for (let cupcake of cupcakes) {
    const $ul = $("#cupcake-list");
    const $cupcakeLi = $(
      `<div data-id=${cupcake.id} id="cupcake-div" ><li id="cupcake-li" class="list-group-item d-flex justify-content-center align-items-center">${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}<button id="delete-button" class="btn btn-sm btn-outline-danger">X</button></li><img class="img-thumbnail" src="${cupcake.image}"</div>`
    );
    $ul.append($cupcakeLi);
  }
}

function showCupcake(cupcake) {
  const $ul = $("#cupcake-list");
  const $cupcakeLi = $(
    `<div data-id=${cupcake.id} id="cupcake-div" ><li id="cupcake-li" class="list-group-item d-flex justify-content-center align-items-center">${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}<button id="delete-button" class="btn btn-sm btn-outline-danger">X</button></li><img class="img-thumbnail" src="${cupcake.image}"></div>`
  );
  $ul.append($cupcakeLi);
}

async function getCupcakes() {
  const res = await axios.get(`api/cupcakes`);
  for (let cupcake of res.data.cupcakes) {
    cupcakes.push(cupcake);
    console.log(cupcakes);
  }
  showCupcakes(cupcakes);
}

async function deleteCupcake(e) {
  e.preventDefault();

  const $parent = $(e.target).parent();
  const $div = $(e.target).closest("div");
  let $id = $div.data('id')
  console.log($id)

  await axios.delete(`/api/cupcakes/${$id}`);
  $div.remove();
}

$("#cupcake-submission-form").on("submit", async function (e) {
  e.preventDefault();
  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image = $("#image").val();
  const res = await axios.post(
    "api/cupcakes",
    (json = {
      flavor,
      size,
      rating,
      image,
    })
  );
  console.log(res);
  const data = res.data.cupcake;
  showCupcake(data);
  $("#cupcake-submission-form").trigger("reset");
});

$("#cupcake-list").on("click", "#delete-button", deleteCupcake);

$(document).ready(getCupcakes);
