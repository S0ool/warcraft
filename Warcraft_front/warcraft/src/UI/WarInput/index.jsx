import React, {useRef} from 'react';

export const Input = ({
                          type, name, placeholder = '', value = '', onChange = () => {
    }, required = true
                      }) => {
    const inputRef = useRef(null);

    const handleInputFlicker = () => {
        if (inputRef.current) {
            inputRef.current.classList.add('input-flicker');
            setTimeout(() => {
                inputRef.current.classList.remove('input-flicker');
            }, 100);
        }
    };

    return (
        <input
            ref={inputRef}
            type={type}
            name={name}
            placeholder={placeholder}
            value={value}
            onChange={(e) => {
                onChange(e);
                handleInputFlicker();
            }}
            required={required}
            className="custom-input"
        />
    );
};


