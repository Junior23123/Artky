import { api } from "@/boot/axios";

export function createProduct(params) {
  return api.post("/product", params);
}

export function getProducts() {
  return api.get("/product");
}

export function deleteProduct(id) {
  return api.get("/product/" + id);
}
