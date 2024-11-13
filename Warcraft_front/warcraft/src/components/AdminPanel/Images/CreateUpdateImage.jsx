import {createImageAxios, updateImageAxios} from "../../../axios/AdminAxios/Images.jsx";
import {Input} from "../../../UI/WarInput/index.jsx";
import styles from "./styles.module.css"
import {useEffect, useState} from "react";

export const CreateUpdateImage = ({
                                      action = 'create',
                                      imageData = {
                                          id: '',
                                          name: '',
                                          description: '',
                                          image: ''
                                      },loadData='',openModal=''

                                  }) => {
    const url = imageData.image;
    const fileName = url.substring(url.lastIndexOf('/') + 1);
    const [imgFile, setImgFile] = useState(fileName);
    const newForm = {...imageData};
    newForm.image = '';
    const [formData, setFormData] = useState(newForm);



    const create = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        createImageAxios(formData);
        loadData();
        openModal()

    };
    const update = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        updateImageAxios(imageData.id, formData);
        if(loadData){
            loadData();
        }
    };
      const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
          console.log(formData);
          console.log({[e.target.name]: e.target.value})
    };


    return (
        <>
            <form className={styles.form} onSubmit={(e) => action == 'create' ? create(e) : update(e)}>
                <Input
                    onChange={handleChange}
                    value={formData?.name}
                    type="text"
                    name="name"
                    placeholder="Name"
                    required={false}/>
                <Input
                    onChange={handleChange} value={formData?.description} type="text" name="description"
                    placeholder="Description"
                    required={false}/>
                {imgFile && <p className={styles.image_desc}>{imgFile}</p>}
                <Input type="file" name="image" onChange={handleChange} value={action=='create'?formData.image:''} required={action=='create'}/>
                <button className={styles.form_btn}>Создать</button>

            </form>

        </>
    )
};