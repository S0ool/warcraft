import styles from "./styles.module.css";
import {Await, Link} from "react-router-dom";
import {ImageItem} from "./image_item.jsx";
import {Suspense, useEffect, useState} from "react";
import {getImagesAxios} from "../../../axios/AdminAxios/Images.jsx";
import {Loader} from "../../../UI/Loader/index.jsx";

export const Images = () => {
    const [images, setImages] = useState([]);


    const [randomColor, setRandomColor] = useState('');
    const [isLoading, setIsLoading] = useState(true);

    const loadData = async () => {
        const response = await getImagesAxios();
        console.log(response);
        return response.data;
    };

    function getRandomColor() {
        return `#${Math.floor(Math.random() * 16777215).toString(16)}`
    }

    useEffect(() => {
        setRandomColor(getRandomColor());
        loadData().then((data) => {
            setTimeout(() => {
                setIsLoading(false);
            }, 2000);
        });
    }, []);


    return (
        <div className={styles.all}>
            <div className={styles.bg}/>
            <h2 className={styles.h2 + ' ' + 'greeting_text'}>Images</h2>
            <Link className={styles.create} to={'/admin/images/create'}>Click to create image</Link>
            <div className={styles.container}>
                {isLoading ? (
                    <div className="loader-container">
                        <Loader/>
                    </div>
                ) : (
                    <Suspense fallback={<Loader/>}>
                        <Await
                            resolve={items}
                            errorElement={<div>Could not load reviews 😬</div>}
                        >
                            {(resolvedData) => {
                                return resolvedData.map((item) => (
                                    <ImageItem image={item}/>
                                ))
                            }}
                        </Await>
                    </Suspense>
                )}

            </div>
        </div>


    )
};