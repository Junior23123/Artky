import { api } from "@/boot/axios";

export function login(params) {
  return api.post("/login", params);
}


export function create(params) {
  return api.post("/register/registrar", params);
}