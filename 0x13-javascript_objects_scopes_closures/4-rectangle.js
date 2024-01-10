#!/usr/bin/node

class Rectangle {
  constructor(width, height) {
    if (width <= 0 || height <= 0) {
      const empty = Object.create(Rectangle.prototype);
      return empty;
    } else {
      this.width = width;
      this.height = height;
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
