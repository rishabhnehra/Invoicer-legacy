import renderer from 'react-test-renderer';
import { render, screen } from '@testing-library/react';
import { Button } from '../Button';

describe("<Button />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<Button>From Snapshot</Button>);
        expect(tree.toJSON()).toMatchSnapshot();
    });
    it("should render button with \"This is buttton\" text", () => {
        render(<Button>This is button</Button>);
        expect(screen.getByText('This is button')).toBeInTheDocument();
    });
});