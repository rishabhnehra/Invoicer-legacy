import './TextInput.css';

export type TextInputProps = {
    placeholder: string,
    onClick: () => void
}

export const TextInput: React.FC<TextInputProps> = ({ placeholder, ...rest }) => {
    return <input
        className="TextInput"
        placeholder={placeholder}
        {...rest}
    />
}