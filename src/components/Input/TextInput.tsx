import './TextInput.css';

export type TextInputProps = {
    placeholder: string,
    type: string,
    id?: string,
    labelText?: string,
    onClick?: () => void,
    onChange?: () => void
}

export const TextInput: React.FC<TextInputProps> = ({ 
    placeholder,
    id,
    type,
    labelText,
    onClick,
    onChange
}) => {
    return <>
        {labelText && <label htmlFor={id}>{labelText} </label>}
        <input
            className="TextInput"
            id={id}
            placeholder={placeholder}
            type={type}
            onClick={onClick}
            onChange={onChange}
        />
    </>
}