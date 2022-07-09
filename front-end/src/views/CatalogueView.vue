<template>
  <div class="catalogue">
    <div class="catalogue-title">¿Qué te gusta?</div>

    <div class="catalogue-carousel">
      <q-carousel swipeable animated v-model="slide" thumbnails infinite>
        <q-carousel-slide
          v-for="item in slides"
          :key="item.name"
          :name="item.name"
          :img-src="item.image"
          class="catalogue-carousel-item"
        >
          <div class="catalogue-carousel-title">{{ item.title }}</div>
          <p class="catalogue-carousel-subtitle">{{ item.subtitle }}</p>
        </q-carousel-slide>
      </q-carousel>
    </div>

    <div class="text-negative text-center">Explora</div>

    <div class="catalogue-product">
      <div class="catalogue-product-title">Catálogo de Artesanía</div>
      <div class="text-center">
        <ButtonBuyProduct  rounded color="negative" label="Comprar" path="/usuario" />
      </div>

      <div class="catalogue-product-grid">
        <div
          v-for="(product, indexProduct) in products"
          :key="`product-item-${indexProduct}`"
          class="catalogue-product-grid-item"
        >
          <div class="catalogue-product-grid-item-name">
            {{ product.title }}
          </div>

          <ItemProductVue
            v-for="(item, indexItem) in product.items"
            :key="`item-${indexItem}`"
            :build="item.build"
            :name="item.name"
            :size="item.size"
            :img="item.image"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import ItemProductVue from "@/components/ItemProduct.vue";
import ButtonBuyProduct from "@/components/ButtonBuyProduct.vue";

export default defineComponent({
  name: "CatalogueView",
  components: {
    ItemProductVue,
    ButtonBuyProduct
  },
  setup() {
    const slide = ref(1);
    const slides = ref([
      {
        title: "Artilugios",
        subtitle: "Artesanales",
        image:
          "https://cdnb.artstation.com/p/assets/images/images/009/573/357/large/jose-luis-castro-c-toritos-vista-02.jpg?1519744305",
        name: 1,
      },
      {
        title: "Jarrones",
        subtitle: "Artesanales",
        image:
          "https://previews.123rf.com/images/keladawy/keladawy1608/keladawy160800021/63909595-vista-frontal-que-muestra-una-composici%C3%B3n-de-jarrones-de-cer%C3%A1mica-artesanales-pintados-art%C3%ADsticos.jpg",
        name: 2,
      },
      {
        title: "Tejidos",
        subtitle: "Artesanales",
        image:
          "https://thumbs.dreamstime.com/b/tejidos-de-seda-tailandeses-artesanales-con-decoraci%C3%B3n-tradicional-adornos-culturales-hermosos-164599188.jpg",
        name: 3,
      },
    ]);

    const products = ref([
      {
        title: "Toritos de Pucará",
        items: [
          {
            image:
              "https://www.argentariaperu.com/wp-content/uploads/2019/11/MG_5605-600x600.jpg",
            name: "Torito Azul",
            size: "15 cm",
            build: "Pintado a mano",
          },
          {
            image:
              "https://greenhouse.com.pe/1229-large_default/torito-de-pucara-rojo-con-suculenta.jpg",
            name: "Torito Rojo",
            size: "16 cm",
            build: "Pintado a mano",
          },
          {
            image:
              "https://i.linio.com/p/d09a2d653d6e44f568bb461ebd58cff3-product.jpg",
            name: "Torito Turquesa",
            size: "17 cm",
            build: "Pintado a mano",
          },
        ],
      },
      {
        title: "Retablos",
        items: [
          {
            image:
              "https://peru.info/Portals/0/Images/Productos/6/101-imagen-1773229122017.jpg",
            name: "Retablo Ayacucho",
            size: "45 cm",
            build: "Hecho a mano",
          },
          {
            image: "https://pbs.twimg.com/media/FHdHdm2XMAIlbS4.jpg",
            name: "Retablo Piurano",
            size: "45 cm",
            build: "Hecho a mano",
          },
          {
            image:
              "https://i.pinimg.com/originals/3e/17/fe/3e17fe29d842c21136c9499c84232dd0.jpg",
            name: "Retablo Cuzqueño",
            size: "45 cm",
            build: "Hecho a mano",
          },
        ],
      },
      {
        title: "Otros",
        items: [
          {
            image:
              "https://www.yourdesignerwear.com/pub/media/catalog/product/cache/3f8f68f85693802ff1cb8bfb8c71680a/m/u/multicolor-art-silk-potli-purse-roy353509.jpg",
            name: "Mochila Luna",
            size: "45 cm",
            build: "Tejido a mano",
          },
          {
            image:
              "https://d20f60vzbd93dl.cloudfront.net/uploads/tienda_000797/tienda_000797_ad7bb4961739ef4560f349def78e376b8f85ecd0_producto_large_90.png",
            name: "Cerámica",
            size: "45 cm",
            build: "Tejido a mano",
          },
          {
            image:
              "https://d15yqn4xt8exgp.cloudfront.net/media/products/TTP000285/inka-products-tissu-traditionnel-du-cusco-tisse-main-motifs-ethniques-4-20210925021840.jpeg",
            name: "Funda Almohada",
            size: "45 cm",
            build: "Tejido a mano",
          },
        ],
      },
    ]);

    return {
      slide,
      slides,
      products,
    };
  },
});
</script>

<style scoped>
.catalogue-carousel {
  max-width: 900px;
  margin: 20px auto;
}

.catalogue-carousel-item {
  position: relative;
}

.catalogue-carousel-title {
  font-size: 4rem;
  color: white;
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.catalogue-carousel-subtitle {
  font-size: 3rem;
  color: white;
  font-family: "Dancing Script", cursive;
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.catalogue-title {
  text-align: center;
  margin: 20px 0;
  font-size: 40px;
  font-family: "Dancing Script", cursive;
  font-weight: bold;
}

.catalogue-product {
  padding: 0 100px;
  padding-bottom: 100px;
}

.catalogue-product-title {
  text-align: center;
  font-size: 4rem;
  margin: 30px 0;
  font-weight: bold;
}

.catalogue-product-grid {
  display: flex;
  gap: 50px;
  justify-content: center;
}

@media screen and (max-width: 900px) {
  .catalogue-product-grid {
    flex-direction: column;
    gap: 0px;
  }

  .catalogue-product {
    padding: 0 30px;
    padding-bottom: 100px;
  }
  .catalogue-carousel {
    margin: 20px;
  }
}

.catalogue-product-grid-item {
  width: 100%;
}

.catalogue-product-grid-item-name {
  margin: 30px 0;
  font-size: 3rem;
  text-align: center;
}
</style>
