import React, {useEffect, useState} from "react";
import styles from "./styles.module.css";
import Loading from "../../../public/User/logo.webp";
export const Loader = () => {
    const [loadingText, setLoadingText] = useState("Loading");

    useEffect(() => {
        const interval = setInterval(() => {
            setLoadingText(prevText => {
                if (prevText === 'Loading...') {
                    return 'Loading';
                } else {
                    return prevText + '.';
                }
            });
        }, 300);

        // Очистка интервала при размонтировании компонента
        return () => clearInterval(interval);
    }, []);
    return (
        <div className={styles.loaderContainer}>
            <div className={styles.logo}>
                <img
                    className={styles.warLogo}
                    src={Loading ? Loading : ""}
                    alt='load'/>
            </div>
            <div className={styles.loadingBar}>
                <div className={styles.bg}></div>
                <div className={styles.loadingProgress}></div>
            </div>
            <p className={styles.loadingText}>{loadingText}</p>
        </div>
    );
};

