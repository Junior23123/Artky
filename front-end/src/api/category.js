import { api } from "@/boot/axios";

export function createCategory(params) {
  return api.post("/category", params);
}

export function getCategories() {
  return api.get("/category");
}
