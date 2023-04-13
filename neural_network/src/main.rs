use image::*;

fn main() {
  const IMAGE_PIXEL_AMOUNT: usize = 784;

  let mut input_layer: Vec<&Luma<u8>> = Vec::with_capacity(IMAGE_PIXEL_AMOUNT);

  let image_to_load = image::open("../../input_image/test_image.bmp").expect("test image not found").to_luma8();

  for pixel in image_to_load.pixels() { 
    input_layer.push(pixel);

  }

}
