<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Stocks</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Stock</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">SYMB</th>
              <th scope="col">CurrPrice</th>
              <th scope="col">YestPrice</th>
              <th scope="col">Recc.</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>foo</td>
              <td>bar</td>
              <td>foobar</td>
              <td>foobarbaz</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-danger btn-sm">Sell</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
