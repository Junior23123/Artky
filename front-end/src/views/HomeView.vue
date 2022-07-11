<template>
  <div class="home">
    <div class="row justify-center">
      <div class="col-xs-12 col-sm-6 col-md-4">
        <div class="home-header">
          <div class="home-title">Comunidad de Artesanos</div>
          <q-btn
            class="text-bold"
            style="margin-bottom: 100px"
            label="MIRA EL CATÁLOGO"
            color="negative"
            rounded
            to="/catalogo"
          />
          <div class="row">
            <div class="text-center q-mr-md" style="width: 100px">
              <span style="font-size: 40px" class="lnr lnr-store"></span>
              <ButtonBuyProduct
                class="text-bold"
                label="comprar"
                flat
                color="negative"
                path="/usuario"
              />
            </div>
            <div class="text-center">
              <span
                style="font-size: 40px; display: block"
                class="lnr lnr-tag q-mb-sm"
              ></span>
              <q-btn
                color="negative"
                class="text-bold"
                flat
                label="Vender"
                href="https://api.whatsapp.com/send?phone=51940192870&text=%C2%A1Hola!%20Estoy%20interesad@%20en%20vender%20un%20producto%20en%20Artky."
                target="_blank"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="col-xs-12 col-sm-6 col-md-4">
        <q-carousel swipeable animated v-model="slide" thumbnails infinite>
          <q-carousel-slide
            :name="1"
            img-src="https://pbs.twimg.com/media/FOarqasXsAA6TZp?format=jpg&name=small"
          />
          <q-carousel-slide
            :name="2"
            img-src="https://i0.wp.com/molycata.com/wp-content/uploads/Telar_Cintura_B.jpg?resize=650,400"
          />
          <q-carousel-slide
            :name="3"
            img-src="https://pbs.twimg.com/media/D39HKQ3X4AEOftz?format=jpg&name=large"
          />
        </q-carousel>
      </div>
    </div>

    <div class="row justify-center">
      <div class="col-xs-12 bg-white col-sm-6 col-md-4 q-pa-md">
        <div class="home-img-1"></div>
      </div>
      <div class="col-xs-12 bg-white col-sm-6 col-md-4 q-pa-md">
        <div style="max-width: 400px">
          <div class="text-negative q-ml-lg margin-bottom">Sobre Artky</div>

          <div class="text-h2 text-bold q-ml-lg margin-bottom">
            Bienvenid@ a Artky
          </div>

          <p class="text-weight-light q-ml-lg margin-bottom">
            En Artky buscamos reinvindicar la artesanía peruana, a través de un
            espacio que difunde las creaciones de nuestros artesanos asociados y
            crea una comunidad de apoyo mutuo entre ellos. Aquí podrás encontrar
            el catálogo de artesanías de los miembros de nuestra comunidad. Si
            quieres unirte a la comunidad de artesanos, puedes registrarte al
            final de la página.
          </p>

          <div class="text-h3 q-ml-lg margin-bottom">
            Algunas piezas destacadas
          </div>

          <div class="row">
            <div class="col">
              <img
                class="home-img-part"
                src="https://greenhouse.com.pe/1228-large_default/torito-de-pucara-negro-con-suculenta.jpg"
              />
              <div class="text-negative text-h6 text-center">
                Toritos de Pucará
              </div>
            </div>
            <div class="col">
              <img
                class="home-img-part"
                src="https://gestion.pe/resizer/uGATgJL3yYS8LcrBIExf4jDrtFA=/1200x1200/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/ZBKVBH3SZVH3NGXZUHY4PBAS4E.JPG"
              />
              <div class="text-negative text-h6 text-center">
                Mini Iglesia de Barro
              </div>
            </div>
            <div class="col">
              <img
                class="home-img-part"
                src="https://pbs.twimg.com/media/ElXRwMMX0AAoM96.png"
              />
              <div class="text-negative text-h6 text-center">
                Retablo Ayacuchano
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="text-negative q-ma-md text-center">explora</div>

    <div class="text-h2 text-center text-bold">
      Encuentra en nuestro catálogo...
    </div>

    <div class="home-catalogue">
      <div class="home-catalogue-product">
        <div class="text-h4">Toritos de Pucará</div>
        <div class="home-catalogue-product-item">
          <img
            src="https://www.argentariaperu.com/wp-content/uploads/2019/11/MG_5605-600x600.jpg"
            alt=""
          />
          <div class="text-h5">Torito Azul</div>

          <div class="text-h5 text-grey home-catalogue-product-item-price">
            S/70
          </div>
        </div>
        <div class="text-weight-light">Art: Julio Flores</div>
      </div>
      <div class="home-catalogue-product">
        <div class="text-h4">Retablos</div>
        <div class="home-catalogue-product-item">
          <img
            src="https://peru.info/Portals/0/Images/Productos/6/101-imagen-1773229122017.jpg"
            alt=""
          />
          <div class="text-h5">Retablo 30 cm</div>

          <div class="text-h5 text-grey home-catalogue-product-item-price">
            S/275
          </div>
        </div>
        <div class="text-weight-light">Fiesta en Huamanga</div>
      </div>
      <div class="home-catalogue-product">
        <div class="text-h4">Otros</div>
        <div class="home-catalogue-product-item">
          <img
            src="https://www.argentariaperu.com/wp-content/uploads/2019/11/MG_5605-600x600.jpg"
            alt=""
          />
          <div class="text-h5">Mochila Luna</div>

          <div class="text-h5 text-grey home-catalogue-product-item-price">
            S/50
          </div>
        </div>
        <div class="text-weight-light">Art: Juana Lopez</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import ButtonBuyProduct from "@/components/ButtonBuyProduct.vue";
export default {
  name: "HomeView",
  components: {
    ButtonBuyProduct,
  },
  setup() {
    const slide = ref(1);
    return { slide };
  },
};
</script>

<style scoped>
.home {
  padding: 30px;
  max-width: 100%;
}
.home-title {
  font-size: 3.5rem;
  font-weight: 300;
  line-height: 1.2;
  margin-bottom: 3rem !important;
}

.home-header {
  width: 350px;
}

.home-img-1 {
  background-image: url(https://tudiariohuanuco.pe/wp-content/uploads/2020/11/artesanos-9.jpeg);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  float: right;
  width: 350px;
  height: 100%;
}

@media screen and (max-width: 600px) {
  .home-img-1 {
    height: 440px;
    width: 100%;
    padding: 0 !important;
  }
}

.home-img-part {
  height: 130px;
  width: 90%;
}

.margin-bottom {
  margin-bottom: 50px;
}

.home-catalogue {
  display: flex;
  gap: 50px;
  max-width: 1240px;
  margin: 0 auto;
  text-align: center;
  margin-bottom: 50px;
}

.home-catalogue-product {
  width: 100%;
  margin-top: 50px;
  padding-bottom: 20px;
  border-bottom: 1px dashed grey;
}

.home-catalogue-product-item img {
  border-radius: 50%;
  width: 100px;
  height: 100px;
}

.home-catalogue-product-item {
  display: flex;
  align-items: center;
  margin-top: 30px;
  gap: 20px;
}

@media screen and (max-width: 900px) {
  .home-catalogue {
    flex-direction: column;
    gap: 0px;
  }

  .home-catalogue-product-item-price {
    width: 100%;
    text-align: end;
  }
}
</style>
