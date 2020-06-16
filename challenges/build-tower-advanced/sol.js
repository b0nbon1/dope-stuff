function towerBuilder(nFloors, nBlockSz) {i
  var lastFloor = nFloors * nBlockSz[0] * 2 - nBlockSz[0];
  var tower = [];
  var floor = 0;
  var space = " ";
  var strk = "*";
  for(var i = 0; i < nFloors * nBlockSz[1]; i++) {
    let lenf = "";
    if(i % nBlockSz[1] == 0) floor += 1;
    let width = floor * nBlockSz[0] * 2 - nBlockSz[0];
    let spaceWidth = (lastFloor - width)/2;
    lenf += space.repeat(spaceWidth);
    lenf += strk.repeat(width);
    lenf += space.repeat(spaceWidth);
    console.log(lenf.length, spaceWidth, width, floor);
    tower.push(lenf);
  }

  return tower;
}

const built = towerBuilder(3, [4, 2])

built.forEach((item) => {
  console.log(item);
})
