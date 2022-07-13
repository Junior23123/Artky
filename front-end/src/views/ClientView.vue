<template>
  <div class="usuario">
    <div class="usuario-title">Interfaz de compra</div>

    <div class="usuario-message-welcome">
      Bienvenid@, {{ storeSession.getUser?.name || "" }}
    </div>

    <div class="usuario-category">
      <img
        v-for="(image, index) in images"
        :key="index"
        class="usuario-category-item"
        :src="image"
        alt="image-category"
      />
    </div>

    <div class="table   ">
      <q-table :columns="columns" title="Productos" :rows="rowsProducts">
      <template v-slot:body-cell-option="props">
          <q-td :props="props">
            <q-btn
              color="purple"
              icon="local_grocery_store"
              href="https://api.whatsapp.com/send?phone=51940192870&text=%C2%A1Hola!%20Estoy%20interesad@%20en%20vender%20un%20producto%20en%20Artky."
              fab-mini
              flat
              @click="handleDeleteProduct(props.row.id)"
            />
          </q-td> </template
      >
      ></q-table>
    </div>
  </div>
</template>

<script>
import { computed, defineComponent, onMounted, reactive, ref } from "vue";
import { useStoreSession } from "@/store/session";
import { useStoreCategory } from "@/store/category";
import { useStoreProduct } from "@/store/product";

export default defineComponent({
  name: "ClientView",
  setup() {
    const images = [
      "https://greenhouse.com.pe/1228-large_default/torito-de-pucara-negro-con-suculenta.jpg",
      "https://gestion.pe/resizer/uGATgJL3yYS8LcrBIExf4jDrtFA=/1200x1200/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/ZBKVBH3SZVH3NGXZUHY4PBAS4E.JPG",
      "https://pbs.twimg.com/media/ElXRwMMX0AAoM96.png",
    ];

    const columns = [
      {
        name: "id",
        field: "id",
        label: "#",
      },
      {
        name: "product",
        field: "product",
        label: "Producto",
      },
      {
        name: "price",
        field: "price",
        label: "Precio",
      },
      {
        name: "option",
        field: "option",
        label: "Opciones",
      },
    ];

    const modal = ref({ open: false, type: "product" });
    const categoryForm = reactive({ name: "" });
    const productForm = reactive({ name: "", price: 0, categoria: "" });

    const storeSession = useStoreSession();
    const storeCategory = useStoreCategory();
    const storeProduct = useStoreProduct();

    const handleCloseModal = () => {
      modal.value.open = false;
    };

    const handleOpenModal = (type) => {
      modal.value.open = true;
      modal.value.type = type;
    };

    const handleForm = async () => {
      if (modal.value.type == "category") {
        await storeCategory.fetchCreateCategory({ name: categoryForm.name });
        await storeCategory.fetchGetCategories();
      }

      if (modal.value.type == "product") {
        await storeProduct.fetchCreateProduct({
          name: productForm.name,
          precio: productForm.price,
          categoria: productForm.categoria?.value,
        });
        await storeProduct.fetchGetProducts();
      }

      handleCloseModal();
    };

    const categoriesOptions = computed(() => {
      return storeCategory.getCategories.map((category) => {
        return { label: category.nombre_categoria, value: category.id };
      });
    });

    const rowsProducts = computed(() => {
      return storeProduct.getProducts.map((product) => {
        return {
          product: product.producto,
          price: product.precio,
          id: product.id,
        };
      });
    });

    const handleDeleteProduct = async (id) => {
      await storeProduct.fetchDeleteProduct(id);
      await storeProduct.fetchGetProducts();
    };

    onMounted(async () => {
      await storeCategory.fetchGetCategories();
      await storeProduct.fetchGetProducts();

      if (storeCategory.getCategories.length > 0) {
        productForm.categoria = {
          label: storeCategory.getCategories[0].nombre_categoria,
          value: storeCategory.getCategories[0].id,
        };
      }
    });

    return {
      images,
      storeSession,
      columns,
      modal,
      handleCloseModal,
      handleOpenModal,
      handleForm,
      categoryForm,
      productForm,
      categoriesOptions,
      rowsProducts,
      handleDeleteProduct,
    };
  },
});
</script>

<style scoped>
.usuario {
  padding: 30px;
}
.usuario-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.usuario-message-welcome {
  font-size: 1rem;
  margin-bottom: 20px;
}

.usuario-category {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.usuario-category-item {
  height: 200px;
  width: 100%;
  background-size: auto;
  background-position: center;
}

.usuario-modal-card {
  width: 400px;
}
</style>
