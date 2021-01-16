import { Cards, TextInput, Button } from '../../index';
import './Login.scss';

export type LoginProps = {
    onClick?: () => void;
    onChange?: () => void;
    onClickGoogleHandler?: () => void;
}

export const Login: React.FC<LoginProps> = ({
    onClickGoogleHandler,
    onClick,
    onChange
}) => <Cards.BlankCard className="Login">
        <header>
            <h3>Login</h3>
        </header>
        <form>
            <div className="form-item">
                <TextInput type="email" placeholder="Email" onChange={onChange} />
            </div>
            <div className="form-item">
                <TextInput type="password" placeholder="Password" onChange={onChange} />
            </div>
            <div className="form-item__submit">
                <Button onClick={onClick}>Continue</Button>
            </div>
        </form>
        <hr />
        <div className="form-item__google-login">
            <Button onClick={onClickGoogleHandler}>Login with Google</Button>
        </div>
    </Cards.BlankCard>