import {createImageAxios, updateImageAxios} from "../../../axios/AdminAxios/Images.jsx";
import {Input} from "../../../UI/WarInput/index.jsx";

export const CreateUpdateImage = ({
                                      action = 'create',
                                      imageData = {
                                          id: '',
                                          name: '',
                                          description: '',
                                          image: ''
                                      }
                                  }) => {
    const create = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        createImageAxios(formData);
    };
    const update = (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        updateImageAxios(imageData.id, formData);
    }
    return (
        <>
            <h2>Create Image</h2>
            <form onSubmit={(e) => action == 'create' ? create(e) : update(e)}>
                <Input value={imageData.name} type="text" name="name" placeholder="Name" required={false}/>
                <Input value={imageData.description} type="text" name="description" placeholder="Description"
                       required={false}/>
                <Input type="file" name="image" value={imageData.image}/>


            </form>

        </>
    )
};