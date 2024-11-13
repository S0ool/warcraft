import styles from "./styles.module.css";
import {Await} from "react-router-dom";
import {ImageItem} from "./image_item.jsx";
import {Suspense, useEffect, useState, useRef} from "react";
import {getImagesAxios} from "../../../axios/AdminAxios/Images.jsx";
import {Loader} from "../../../UI/Loader/index.jsx";
import {CreateUpdateImage} from "./CreateUpdateImage.jsx";

export const Images = ({is_admin = false}) => {
    const [images, setImages] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isLoading, setIsLoading] = useState(true);
    const [imgModalOpen, setImgModalOpen] = useState(false);
    const [currentImg, setCurrentImg] = useState('');
    const [currentImgIndex, setCurrentImgIndex] = useState(null);
    const [lastScrollY, setLastScrollY] = useState(window.scrollY);
    const imageRefs = useRef([]);
    const imageContRef = useRef();

    const loadData = async () => {
        const response = await getImagesAxios();
        setImages(response);
        setIsLoading(false);
    };

    const openModal = () => {
        setIsModalOpen(!isModalOpen);
    };

    const openImgModal = (image, index) => {
        setCurrentImg(image);
        setCurrentImgIndex(index);
        setImgModalOpen(true);
    };

    const closeImgModal = () => {
        setImgModalOpen(false);
        if (currentImgIndex !== null && imageRefs.current[currentImgIndex]) {
            imageRefs.current[currentImgIndex].scrollIntoView({ behavior: "smooth", block: "center" });
        }
    };

    useEffect(() => {
        loadData();
    }, []);
useEffect(() => {
    setTimeout(() => {
        const container = imageContRef.current;

        if (!container) {
            console.log("Container ref not available after delay");
            return;
        }

        const handleScroll = () => {
            const currentScrollY = container.scrollTop;

            if (currentScrollY > lastScrollY) {
                container.classList.remove("scrollUp");
                container.classList.add("scrollDown");

            } else if (currentScrollY < lastScrollY) {
                container.classList.remove("scrollDown");
                container.classList.add("scrollUp");

            }

            setLastScrollY(currentScrollY);
        };

        container.addEventListener("scroll", handleScroll);

        return () => {
            container.removeEventListener("scroll", handleScroll);
            container.classList.remove("scrollDown", "scrollUp");
        };
    }, 100);
}, [lastScrollY, imageContRef.current]);



    return (
        <div className={styles.all}>
            <div className={styles.bg}/>
            <h2 className={`${styles.h2} greeting_text`}>Изображения</h2>
            {is_admin && (
                <button className={styles.create} onClick={openModal}>
                    {isModalOpen ? "Закрыть" : "Создать изображение"}
                </button>
            )}

            <div className={styles.container}>
                {isLoading ? (
                    <div className="loader-container">
                        <Loader />
                    </div>
                ) : (
                    <Suspense fallback={<Loader />}>
                        <Await resolve={images} errorElement={<div>Could not load data -->:( </div>}>
                            {imgModalOpen ? (
                                <div className={styles.imgModal}>
                                    <img className={styles.imgModalImage} onClick={closeImgModal} src={currentImg} alt={currentImg} />
                                </div>
                            ) : (
                                <div className={styles.imageContainer} ref={imageContRef}>
                                    {isModalOpen ? (
                                        <div className={styles.modal}>
                                            <h2>Создание изображения</h2>
                                            <CreateUpdateImage action="create" loadData={loadData} openModal={openModal}/>
                                        </div>
                                    ) : (
                                        images.map((image, index) => (
                                            <ImageItem
                                                key={image.id}
                                                image={image}
                                                is_admin={is_admin}
                                                setImgModalOpen={() => openImgModal(image.image, index)}
                                                ref={(el) => (imageRefs.current[index] = el)} // Присваиваем ref каждому изображению
                                            />
                                        ))
                                    )}
                                </div>
                            )}
                        </Await>
                    </Suspense>
                )}
            </div>
        </div>
    );
};
